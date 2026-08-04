# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T20:06:19.339287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0492` n `12`; crypto_alt avg `-0.0833` n `230`; crypto_major avg `0.0075` n `8`; equity avg `0.1699` n `107`; fx avg `-0.0008` n `6`; index avg `0.0298` n `25`; metal avg `0.0111` n `20`; unknown avg `0.074` n `782`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0672` n `230`; crypto_major avg `0.0509` n `8`; equity avg `-0.082` n `107`; fx avg `-0.0028` n `6`; index avg `0.0209` n `25`; metal avg `-0.0441` n `20`; unknown avg `0.0152` n `782`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `0.3154` n `230`; crypto_major avg `0.2827` n `8`; equity avg `0.4865` n `107`; fx avg `0.0546` n `6`; index avg `0.1981` n `25`; metal avg `-0.0558` n `20`; unknown avg `-0.1773` n `782`
- 24h: commodity avg `-1.1738` n `12`; crypto_alt avg `-0.0083` n `230`; crypto_major avg `0.4608` n `8`; equity avg `3.9454` n `107`; fx avg `0.1406` n `6`; index avg `0.8595` n `25`; metal avg `0.9311` n `20`; unknown avg `0.4852` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
