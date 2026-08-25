# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T11:37:23.967117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6666` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3569` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.061` n `12`; crypto_alt avg `0.2122` n `231`; crypto_major avg `0.2677` n `8`; equity avg `0.0363` n `122`; fx avg `-0.0004` n `6`; index avg `0.0055` n `25`; metal avg `0.0244` n `20`; unknown avg `0.0695` n `795`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `0.2217` n `231`; crypto_major avg `0.1002` n `8`; equity avg `-0.1404` n `122`; fx avg `-0.0021` n `6`; index avg `-0.015` n `25`; metal avg `0.0575` n `20`; unknown avg `0.0734` n `795`
- 4h: commodity avg `-0.3446` n `12`; crypto_alt avg `-1.05` n `231`; crypto_major avg `-1.2567` n `8`; equity avg `0.4099` n `122`; fx avg `-0.0342` n `6`; index avg `0.1002` n `25`; metal avg `-0.0138` n `20`; unknown avg `-0.1191` n `794`
- 24h: commodity avg `-0.7391` n `12`; crypto_alt avg `-0.5031` n `231`; crypto_major avg `0.1958` n `8`; equity avg `0.385` n `122`; fx avg `0.0079` n `6`; index avg `0.0748` n `25`; metal avg `-0.3143` n `20`; unknown avg `-0.1797` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
