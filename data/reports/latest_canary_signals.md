# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T18:52:27.863562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.097` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `0.1662` n `8`; equity avg `-0.0623` n `94`; fx avg `0.0121` n `6`; index avg `-0.0197` n `25`; metal avg `0.0554` n `20`; unknown avg `0.0321` n `768`
- 1h: commodity avg `0.1274` n `12`; crypto_alt avg `0.1525` n `230`; crypto_major avg `0.2669` n `8`; equity avg `0.1762` n `94`; fx avg `-0.0048` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0317` n `20`; unknown avg `0.0523` n `768`
- 4h: commodity avg `-0.0772` n `12`; crypto_alt avg `-0.6514` n `230`; crypto_major avg `-1.2859` n `8`; equity avg `-0.9724` n `94`; fx avg `-0.0303` n `6`; index avg `-0.1889` n `25`; metal avg `-0.2533` n `20`; unknown avg `-0.0409` n `768`
- 24h: commodity avg `-0.2638` n `12`; crypto_alt avg `-0.9672` n `230`; crypto_major avg `-2.1475` n `8`; equity avg `-3.3953` n `94`; fx avg `-0.1487` n `6`; index avg `-0.4624` n `25`; metal avg `-0.8303` n `20`; unknown avg `-0.3587` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
