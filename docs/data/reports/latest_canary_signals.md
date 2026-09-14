# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T19:18:43.012533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0166` n `233`; crypto_major avg `0.0497` n `8`; equity avg `-0.0903` n `136`; fx avg `0.0094` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0199` n `20`; unknown avg `0.5888` n `908`
- 1h: commodity avg `-0.1283` n `12`; crypto_alt avg `-0.0819` n `233`; crypto_major avg `0.0482` n `8`; equity avg `-0.2627` n `136`; fx avg `-0.0152` n `6`; index avg `-0.0285` n `27`; metal avg `-0.0456` n `20`; unknown avg `0.7567` n `906`
- 4h: commodity avg `-0.3962` n `12`; crypto_alt avg `1.2696` n `233`; crypto_major avg `1.5417` n `8`; equity avg `0.5022` n `136`; fx avg `0.0022` n `6`; index avg `0.1516` n `27`; metal avg `0.151` n `20`; unknown avg `1.138` n `878`
- 24h: commodity avg `0.0875` n `12`; crypto_alt avg `0.5422` n `233`; crypto_major avg `2.5126` n `8`; equity avg `-0.4508` n `136`; fx avg `0.05` n `6`; index avg `-0.1415` n `27`; metal avg `-0.3332` n `20`; unknown avg `3.3217` n `696`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
