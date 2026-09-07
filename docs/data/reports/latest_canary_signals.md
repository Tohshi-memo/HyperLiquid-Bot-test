# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T01:07:50.859220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `12`; crypto_alt avg `-0.4763` n `232`; crypto_major avg `-0.2868` n `8`; equity avg `-0.0182` n `134`; fx avg `-0.0238` n `6`; index avg `-0.0076` n `26`; metal avg `-0.1036` n `20`; unknown avg `0.4814` n `792`
- 1h: commodity avg `-0.0305` n `12`; crypto_alt avg `-0.5371` n `232`; crypto_major avg `-0.4373` n `8`; equity avg `0.0022` n `134`; fx avg `-0.1437` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0661` n `20`; unknown avg `0.3781` n `784`
- 4h: commodity avg `-0.0334` n `12`; crypto_alt avg `0.0853` n `232`; crypto_major avg `-0.0766` n `8`; equity avg `0.0565` n `134`; fx avg `-0.1352` n `6`; index avg `-0.0186` n `26`; metal avg `-0.1355` n `20`; unknown avg `0.51` n `783`
- 24h: commodity avg `-0.087` n `12`; crypto_alt avg `0.4834` n `232`; crypto_major avg `0.3183` n `8`; equity avg `0.2887` n `134`; fx avg `-0.085` n `6`; index avg `-0.0057` n `26`; metal avg `-0.1532` n `20`; unknown avg `150.7982` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
