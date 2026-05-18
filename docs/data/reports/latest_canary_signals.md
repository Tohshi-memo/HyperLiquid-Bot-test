# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T00:07:16.964593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2367` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1599` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2585` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1648` n `12`; crypto_alt avg `0.0136` n `228`; crypto_major avg `0.1364` n `8`; equity avg `-0.8311` n `66`; fx avg `0.0124` n `5`; index avg `-0.3874` n `23`; metal avg `-0.2527` n `18`; unknown avg `-0.2521` n `383`
- 1h: commodity avg `0.3123` n `12`; crypto_alt avg `-1.725` n `228`; crypto_major avg `-0.943` n `8`; equity avg `-0.8034` n `66`; fx avg `0.0428` n `5`; index avg `-0.5566` n `23`; metal avg `-0.2975` n `18`; unknown avg `0.5299` n `383`
- 4h: commodity avg `0.3895` n `12`; crypto_alt avg `-2.602` n `228`; crypto_major avg `-1.8472` n `8`; equity avg `-0.7401` n `66`; fx avg `0.0234` n `5`; index avg `-0.5887` n `23`; metal avg `0.3127` n `18`; unknown avg `1.1239` n `383`
- 24h: commodity avg `2.1883` n `12`; crypto_alt avg `-11.3999` n `228`; crypto_major avg `-3.0075` n `8`; equity avg `-3.673` n `65`; fx avg `-0.1308` n `5`; index avg `-2.0845` n `23`; metal avg `-5.6755` n `18`; unknown avg `550.1126` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
