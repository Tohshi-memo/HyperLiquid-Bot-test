# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T15:52:27.966121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6281` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.0128` n `230`; crypto_major avg `0.0369` n `8`; equity avg `0.321` n `103`; fx avg `0.0275` n `6`; index avg `0.0314` n `25`; metal avg `0.0593` n `20`; unknown avg `0.035` n `784`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `0.1498` n `230`; crypto_major avg `0.2067` n `8`; equity avg `-0.0744` n `103`; fx avg `0.0304` n `6`; index avg `0.0002` n `25`; metal avg `0.0629` n `20`; unknown avg `-0.1782` n `784`
- 4h: commodity avg `0.1132` n `12`; crypto_alt avg `0.9555` n `230`; crypto_major avg `1.3963` n `8`; equity avg `2.5575` n `103`; fx avg `-0.0027` n `6`; index avg `0.2053` n `25`; metal avg `-0.2318` n `20`; unknown avg `0.0129` n `784`
- 24h: commodity avg `-0.2289` n `12`; crypto_alt avg `0.1858` n `230`; crypto_major avg `1.1473` n `8`; equity avg `1.5066` n `102`; fx avg `-0.1648` n `6`; index avg `-0.0099` n `25`; metal avg `-0.4192` n `20`; unknown avg `0.0799` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
