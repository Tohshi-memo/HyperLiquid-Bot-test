# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T02:37:26.493036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1461` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1548` n `230`; crypto_major avg `-0.1426` n `8`; equity avg `-0.1262` n `102`; fx avg `0.0028` n `6`; index avg `-0.0293` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0275` n `779`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `-0.7252` n `230`; crypto_major avg `-0.8014` n `8`; equity avg `-0.7433` n `102`; fx avg `-0.0286` n `6`; index avg `-0.1308` n `25`; metal avg `-0.0061` n `20`; unknown avg `1.3005` n `779`
- 4h: commodity avg `-0.27` n `12`; crypto_alt avg `-0.5385` n `230`; crypto_major avg `-0.9993` n `8`; equity avg `0.1886` n `102`; fx avg `0.1667` n `6`; index avg `0.1468` n `25`; metal avg `-0.2467` n `20`; unknown avg `0.8571` n `779`
- 24h: commodity avg `-0.1412` n `12`; crypto_alt avg `-0.2089` n `230`; crypto_major avg `0.4448` n `8`; equity avg `7.1613` n `102`; fx avg `-0.1983` n `6`; index avg `0.9282` n `25`; metal avg `0.3508` n `20`; unknown avg `0.0317` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
