# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T11:22:28.978210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `13`; crypto_alt avg `0.0038` n `234`; crypto_major avg `-0.0212` n `8`; equity avg `-0.0901` n `142`; fx avg `0.0196` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0196` n `20`; unknown avg `-0.1462` n `985`
- 1h: commodity avg `-0.0532` n `13`; crypto_alt avg `0.0808` n `234`; crypto_major avg `0.2123` n `8`; equity avg `-0.0698` n `142`; fx avg `0.012` n `6`; index avg `0.0402` n `26`; metal avg `0.1399` n `20`; unknown avg `-0.5254` n `983`
- 4h: commodity avg `-0.4638` n `13`; crypto_alt avg `0.4959` n `234`; crypto_major avg `0.7652` n `8`; equity avg `0.2056` n `142`; fx avg `-0.0674` n `6`; index avg `0.0911` n `26`; metal avg `-0.0269` n `20`; unknown avg `-0.5631` n `907`
- 24h: commodity avg `-0.6368` n `13`; crypto_alt avg `1.9627` n `234`; crypto_major avg `2.146` n `8`; equity avg `0.9871` n `142`; fx avg `-0.3199` n `6`; index avg `0.2325` n `26`; metal avg `0.1261` n `20`; unknown avg `0.1232` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
