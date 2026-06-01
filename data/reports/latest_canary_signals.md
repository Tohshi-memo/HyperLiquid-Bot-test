# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T04:52:19.304676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2853` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.2863` n `228`; crypto_major avg `0.0522` n `8`; equity avg `0.0349` n `69`; fx avg `0.0091` n `6`; index avg `0.0689` n `23`; metal avg `-0.0421` n `18`; unknown avg `-0.1054` n `422`
- 1h: commodity avg `-0.0312` n `12`; crypto_alt avg `-0.83` n `228`; crypto_major avg `-0.5705` n `8`; equity avg `0.0379` n `69`; fx avg `-0.0041` n `6`; index avg `0.0723` n `23`; metal avg `0.1278` n `18`; unknown avg `-0.7255` n `422`
- 4h: commodity avg `0.1544` n `12`; crypto_alt avg `-0.7173` n `228`; crypto_major avg `-0.9522` n `8`; equity avg `0.0618` n `69`; fx avg `0.0342` n `6`; index avg `0.3331` n `23`; metal avg `-0.1714` n `18`; unknown avg `-0.6666` n `421`
- 24h: commodity avg `0.9421` n `12`; crypto_alt avg `0.1181` n `228`; crypto_major avg `-0.7808` n `8`; equity avg `0.5336` n `69`; fx avg `0.0308` n `6`; index avg `0.7952` n `23`; metal avg `0.162` n `18`; unknown avg `1.5401` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2881`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
