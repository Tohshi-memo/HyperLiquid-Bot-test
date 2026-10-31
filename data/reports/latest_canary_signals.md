# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T13:52:26.629292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `0.132` n `238`; crypto_major avg `0.0722` n `8`; equity avg `0.0178` n `156`; fx avg `0.0051` n `6`; index avg `0.001` n `27`; metal avg `0.0033` n `20`; unknown avg `159.0067` n `1262`
- 1h: commodity avg `-0.0712` n `13`; crypto_alt avg `-0.146` n `238`; crypto_major avg `-0.1295` n `8`; equity avg `-0.0376` n `156`; fx avg `0.0035` n `6`; index avg `-0.0096` n `27`; metal avg `0.003` n `20`; unknown avg `-0.1497` n `1256`
- 4h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.3953` n `238`; crypto_major avg `0.3463` n `8`; equity avg `-0.0961` n `156`; fx avg `0.0094` n `6`; index avg `-0.0253` n `27`; metal avg `0.0027` n `20`; unknown avg `205.8371` n `1218`
- 24h: commodity avg `-0.2643` n `13`; crypto_alt avg `1.5159` n `238`; crypto_major avg `0.5178` n `8`; equity avg `-1.0187` n `156`; fx avg `0.0507` n `6`; index avg `-0.1306` n `27`; metal avg `-0.0261` n `20`; unknown avg `2.2619` n `1045`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
