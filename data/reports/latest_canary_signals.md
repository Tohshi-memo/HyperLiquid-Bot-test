# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T06:37:30.909686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.1982` n `230`; crypto_major avg `-0.1849` n `8`; equity avg `-0.1128` n `107`; fx avg `0.0148` n `6`; index avg `-0.0428` n `25`; metal avg `-0.0567` n `20`; unknown avg `-0.0012` n `781`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.0737` n `230`; crypto_major avg `-0.1647` n `8`; equity avg `0.1736` n `107`; fx avg `0.0426` n `6`; index avg `0.0139` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.0023` n `765`
- 4h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.3292` n `230`; crypto_major avg `-0.3238` n `8`; equity avg `0.6475` n `107`; fx avg `0.071` n `6`; index avg `0.0631` n `25`; metal avg `0.057` n `20`; unknown avg `-0.0445` n `764`
- 24h: commodity avg `0.3866` n `12`; crypto_alt avg `1.1534` n `230`; crypto_major avg `1.1928` n `8`; equity avg `2.3068` n `107`; fx avg `0.0281` n `6`; index avg `0.2317` n `25`; metal avg `-0.0274` n `20`; unknown avg `0.182` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
