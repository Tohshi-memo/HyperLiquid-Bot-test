# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T19:07:28.440993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `0.1155` n `8`; equity avg `0.1697` n `108`; fx avg `-0.0066` n `6`; index avg `0.0257` n `25`; metal avg `0.0337` n `20`; unknown avg `-0.0603` n `782`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `-0.0177` n `8`; equity avg `-0.0021` n `108`; fx avg `-0.0044` n `6`; index avg `0.0108` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.0106` n `782`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `0.2123` n `230`; crypto_major avg `0.5104` n `8`; equity avg `0.0293` n `108`; fx avg `0.0067` n `6`; index avg `-0.0302` n `25`; metal avg `0.1057` n `20`; unknown avg `-0.0859` n `782`
- 24h: commodity avg `-0.0832` n `12`; crypto_alt avg `0.6081` n `230`; crypto_major avg `0.961` n `8`; equity avg `-0.3586` n `108`; fx avg `-0.0563` n `6`; index avg `-0.0642` n `25`; metal avg `0.8388` n `20`; unknown avg `0.7915` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
