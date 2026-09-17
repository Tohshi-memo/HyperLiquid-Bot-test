# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T11:52:30.538577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `0.0337` n `234`; crypto_major avg `0.0127` n `8`; equity avg `-0.0537` n `137`; fx avg `0.001` n `6`; index avg `-0.0085` n `27`; metal avg `0.037` n `20`; unknown avg `-0.1825` n `921`
- 1h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0204` n `234`; crypto_major avg `-0.0766` n `8`; equity avg `-0.0936` n `137`; fx avg `-0.0354` n `6`; index avg `0.0093` n `27`; metal avg `0.0424` n `20`; unknown avg `-0.0678` n `919`
- 4h: commodity avg `-0.1921` n `12`; crypto_alt avg `-0.0923` n `234`; crypto_major avg `-0.3359` n `8`; equity avg `0.2916` n `137`; fx avg `-0.0035` n `6`; index avg `0.0556` n `27`; metal avg `-0.0647` n `20`; unknown avg `0.5137` n `911`
- 24h: commodity avg `-0.6234` n `12`; crypto_alt avg `2.3909` n `234`; crypto_major avg `0.4566` n `8`; equity avg `1.1303` n `137`; fx avg `0.0863` n `6`; index avg `0.0921` n `27`; metal avg `-0.1314` n `20`; unknown avg `0.0937` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
