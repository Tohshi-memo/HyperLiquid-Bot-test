# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T16:37:25.314730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3933` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1083` n `13`; crypto_alt avg `0.2749` n `239`; crypto_major avg `0.4092` n `8`; equity avg `0.339` n `168`; fx avg `-0.0088` n `6`; index avg `0.0241` n `27`; metal avg `0.0356` n `20`; unknown avg `6.1995` n `1264`
- 1h: commodity avg `-0.321` n `13`; crypto_alt avg `0.0705` n `239`; crypto_major avg `0.2456` n `8`; equity avg `0.3343` n `168`; fx avg `-0.0307` n `6`; index avg `0.0287` n `27`; metal avg `-0.0504` n `20`; unknown avg `4.2765` n `1256`
- 4h: commodity avg `-0.4289` n `13`; crypto_alt avg `-1.4715` n `239`; crypto_major avg `-1.4069` n `8`; equity avg `-0.3276` n `168`; fx avg `-0.0801` n `6`; index avg `-0.0136` n `27`; metal avg `-0.3855` n `20`; unknown avg `5.6599` n `1251`
- 24h: commodity avg `-0.611` n `13`; crypto_alt avg `0.8583` n `239`; crypto_major avg `1.7572` n `8`; equity avg `3.1945` n `168`; fx avg `-0.1532` n `6`; index avg `0.2842` n `27`; metal avg `0.6934` n `20`; unknown avg `90.5622` n `1035`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
