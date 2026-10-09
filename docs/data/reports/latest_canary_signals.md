# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T00:52:29.338944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `13`; crypto_alt avg `-0.029` n `235`; crypto_major avg `0.0856` n `8`; equity avg `-0.0068` n `150`; fx avg `0.0254` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0425` n `20`; unknown avg `-0.0588` n `1078`
- 1h: commodity avg `-0.0465` n `13`; crypto_alt avg `0.1508` n `235`; crypto_major avg `0.2522` n `8`; equity avg `0.2756` n `150`; fx avg `0.0386` n `6`; index avg `0.0572` n `26`; metal avg `0.0117` n `20`; unknown avg `0.1067` n `1069`
- 4h: commodity avg `0.0131` n `13`; crypto_alt avg `-0.1976` n `235`; crypto_major avg `0.1117` n `8`; equity avg `0.1759` n `150`; fx avg `0.0807` n `6`; index avg `0.0541` n `26`; metal avg `0.1302` n `20`; unknown avg `0.2959` n `1061`
- 24h: commodity avg `0.5409` n `13`; crypto_alt avg `-3.5961` n `235`; crypto_major avg `-3.653` n `8`; equity avg `-2.5911` n `150`; fx avg `0.1888` n `6`; index avg `-0.2661` n `26`; metal avg `0.0683` n `20`; unknown avg `5.8552` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
