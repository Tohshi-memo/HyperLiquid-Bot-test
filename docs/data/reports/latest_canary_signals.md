# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T10:37:36.517618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `0.0634` n `234`; crypto_major avg `0.0245` n `8`; equity avg `-0.0018` n `137`; fx avg `-0.0024` n `6`; index avg `-0.0045` n `27`; metal avg `0.0153` n `20`; unknown avg `0.1097` n `921`
- 1h: commodity avg `-0.1472` n `12`; crypto_alt avg `-0.4153` n `234`; crypto_major avg `-0.6468` n `8`; equity avg `0.0262` n `137`; fx avg `0.0103` n `6`; index avg `0.0214` n `27`; metal avg `0.0227` n `20`; unknown avg `0.3564` n `919`
- 4h: commodity avg `-0.0332` n `12`; crypto_alt avg `0.1283` n `234`; crypto_major avg `-0.0985` n `8`; equity avg `0.7054` n `137`; fx avg `0.0683` n `6`; index avg `0.099` n `27`; metal avg `0.0378` n `20`; unknown avg `-0.0382` n `911`
- 24h: commodity avg `-0.6484` n `12`; crypto_alt avg `2.9562` n `234`; crypto_major avg `1.2968` n `8`; equity avg `1.5545` n `137`; fx avg `0.103` n `6`; index avg `0.1318` n `27`; metal avg `-0.1688` n `20`; unknown avg `0.3114` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
