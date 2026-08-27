# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T14:52:37.789948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1005` n `12`; crypto_alt avg `-0.1313` n `231`; crypto_major avg `0.0183` n `8`; equity avg `-0.2396` n `127`; fx avg `-0.0136` n `6`; index avg `0.0047` n `26`; metal avg `0.0126` n `20`; unknown avg `0.0317` n `791`
- 1h: commodity avg `-0.1381` n `12`; crypto_alt avg `0.6777` n `231`; crypto_major avg `1.177` n `8`; equity avg `-0.0863` n `127`; fx avg `-0.0404` n `6`; index avg `0.0171` n `26`; metal avg `0.1326` n `20`; unknown avg `0.0137` n `791`
- 4h: commodity avg `0.0679` n `12`; crypto_alt avg `1.0592` n `231`; crypto_major avg `1.3109` n `8`; equity avg `-0.4946` n `127`; fx avg `0.006` n `6`; index avg `-0.0161` n `26`; metal avg `0.0689` n `20`; unknown avg `-0.0848` n `791`
- 24h: commodity avg `0.2041` n `12`; crypto_alt avg `3.4169` n `231`; crypto_major avg `4.3028` n `8`; equity avg `1.6523` n `127`; fx avg `-0.058` n `6`; index avg `0.1734` n `26`; metal avg `-0.1353` n `20`; unknown avg `0.7696` n `774`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
