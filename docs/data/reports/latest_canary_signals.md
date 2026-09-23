# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T06:37:26.914949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `0.0422` n `234`; crypto_major avg `0.0415` n `8`; equity avg `0.1289` n `140`; fx avg `0.0105` n `6`; index avg `0.0351` n `26`; metal avg `0.0183` n `20`; unknown avg `-0.0739` n `945`
- 1h: commodity avg `-0.0365` n `12`; crypto_alt avg `0.143` n `234`; crypto_major avg `-0.0687` n `8`; equity avg `0.1705` n `140`; fx avg `0.0444` n `6`; index avg `0.0475` n `26`; metal avg `-0.0305` n `20`; unknown avg `-0.0046` n `927`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `1.1692` n `234`; crypto_major avg `0.4689` n `8`; equity avg `0.3132` n `140`; fx avg `0.055` n `6`; index avg `0.0775` n `26`; metal avg `-0.0453` n `20`; unknown avg `0.1652` n `921`
- 24h: commodity avg `-0.2064` n `12`; crypto_alt avg `4.1389` n `234`; crypto_major avg `2.079` n `8`; equity avg `1.4469` n `140`; fx avg `-0.1411` n `6`; index avg `0.1754` n `26`; metal avg `0.2065` n `20`; unknown avg `2.3885` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
