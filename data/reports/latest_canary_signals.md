# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T05:07:28.951232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.2127` n `234`; crypto_major avg `-0.219` n `8`; equity avg `-0.056` n `137`; fx avg `-0.0011` n `6`; index avg `-0.0102` n `27`; metal avg `0.0141` n `20`; unknown avg `2.71` n `917`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `-0.2148` n `234`; crypto_major avg `-0.3226` n `8`; equity avg `-0.1497` n `137`; fx avg `-0.0085` n `6`; index avg `-0.0355` n `27`; metal avg `-0.0191` n `20`; unknown avg `2.4359` n `911`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `0.0344` n `234`; crypto_major avg `0.069` n `8`; equity avg `0.615` n `137`; fx avg `-0.0381` n `6`; index avg `0.0748` n `27`; metal avg `0.3161` n `20`; unknown avg `1.6782` n `907`
- 24h: commodity avg `0.1682` n `12`; crypto_alt avg `-3.4075` n `234`; crypto_major avg `-3.2756` n `8`; equity avg `-0.3399` n `137`; fx avg `0.1986` n `6`; index avg `0.0395` n `27`; metal avg `0.3857` n `20`; unknown avg `18796.3606` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
