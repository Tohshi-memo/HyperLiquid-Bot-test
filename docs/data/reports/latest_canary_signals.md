# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T12:07:28.963252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1145` n `12`; crypto_alt avg `0.1811` n `234`; crypto_major avg `0.3053` n `8`; equity avg `0.1655` n `137`; fx avg `-0.0142` n `6`; index avg `0.0644` n `27`; metal avg `0.0891` n `20`; unknown avg `0.1728` n `919`
- 1h: commodity avg `-0.1142` n `12`; crypto_alt avg `0.0461` n `234`; crypto_major avg `0.1677` n `8`; equity avg `0.0199` n `137`; fx avg `-0.0061` n `6`; index avg `0.0483` n `27`; metal avg `0.0737` n `20`; unknown avg `-0.3927` n `919`
- 4h: commodity avg `-0.3359` n `12`; crypto_alt avg `0.0858` n `234`; crypto_major avg `-0.1547` n `8`; equity avg `0.3374` n `137`; fx avg `-0.034` n `6`; index avg `0.1388` n `27`; metal avg `0.0606` n `20`; unknown avg `0.3434` n `911`
- 24h: commodity avg `-0.7482` n `12`; crypto_alt avg `2.7054` n `234`; crypto_major avg `0.9306` n `8`; equity avg `1.3003` n `137`; fx avg `0.0735` n `6`; index avg `0.1456` n `27`; metal avg `-0.0222` n `20`; unknown avg `0.3547` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
