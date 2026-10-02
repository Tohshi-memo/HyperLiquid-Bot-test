# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T06:22:26.933219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0705` n `13`; crypto_alt avg `-0.0028` n `234`; crypto_major avg `0.0778` n `8`; equity avg `-0.0541` n `142`; fx avg `0.0032` n `6`; index avg `-0.0138` n `26`; metal avg `-0.022` n `20`; unknown avg `0.9712` n `983`
- 1h: commodity avg `-0.0755` n `13`; crypto_alt avg `-0.0445` n `234`; crypto_major avg `-0.0481` n `8`; equity avg `-0.0664` n `142`; fx avg `-0.0494` n `6`; index avg `-0.0108` n `26`; metal avg `0.0191` n `20`; unknown avg `6.9136` n `953`
- 4h: commodity avg `-0.1352` n `13`; crypto_alt avg `1.1601` n `234`; crypto_major avg `1.4403` n `8`; equity avg `0.1304` n `142`; fx avg `-0.081` n `6`; index avg `0.0252` n `26`; metal avg `0.2658` n `20`; unknown avg `7.8001` n `947`
- 24h: commodity avg `0.2338` n `13`; crypto_alt avg `0.0473` n `234`; crypto_major avg `0.9588` n `8`; equity avg `-0.0723` n `142`; fx avg `-0.2949` n `6`; index avg `-0.0714` n `26`; metal avg `-0.111` n `20`; unknown avg `1143.7557` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
