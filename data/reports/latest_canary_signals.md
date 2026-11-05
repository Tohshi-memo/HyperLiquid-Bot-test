# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T12:37:28.411811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0945` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `-0.3773` n `239`; crypto_major avg `-0.3621` n `8`; equity avg `-0.2401` n `158`; fx avg `-0.0237` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0744` n `20`; unknown avg `0.2993` n `1255`
- 1h: commodity avg `0.1071` n `13`; crypto_alt avg `-0.9706` n `239`; crypto_major avg `-0.7311` n `8`; equity avg `-0.8119` n `158`; fx avg `0.0337` n `6`; index avg `-0.078` n `27`; metal avg `-0.1485` n `20`; unknown avg `0.3415` n `1247`
- 4h: commodity avg `0.4162` n `13`; crypto_alt avg `-1.5166` n `239`; crypto_major avg `-1.2015` n `8`; equity avg `-0.9415` n `158`; fx avg `0.0184` n `6`; index avg `-0.107` n `27`; metal avg `0.0007` n `20`; unknown avg `215.7025` n `1145`
- 24h: commodity avg `-1.0306` n `13`; crypto_alt avg `-0.1379` n `239`; crypto_major avg `1.281` n `8`; equity avg `-2.8985` n `158`; fx avg `-0.0106` n `6`; index avg `-0.2865` n `27`; metal avg `0.5564` n `20`; unknown avg `230.1747` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
