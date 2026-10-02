# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T02:19:59.734114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `0.1096` n `234`; crypto_major avg `-0.0537` n `8`; equity avg `0.0762` n `142`; fx avg `-0.0166` n `6`; index avg `0.0107` n `26`; metal avg `0.0389` n `20`; unknown avg `0.1587` n `985`
- 1h: commodity avg `-0.0163` n `13`; crypto_alt avg `0.9097` n `234`; crypto_major avg `0.6472` n `8`; equity avg `0.1344` n `142`; fx avg `-0.0607` n `6`; index avg `0.0466` n `26`; metal avg `0.0868` n `20`; unknown avg `1.3556` n `983`
- 4h: commodity avg `-0.186` n `13`; crypto_alt avg `0.8507` n `234`; crypto_major avg `0.4623` n `8`; equity avg `0.1856` n `142`; fx avg `-0.0346` n `6`; index avg `0.0598` n `26`; metal avg `-0.1045` n `20`; unknown avg `0.2695` n `977`
- 24h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.455` n `234`; crypto_major avg `0.5172` n `8`; equity avg `0.8508` n `142`; fx avg `-0.2316` n `6`; index avg `0.1232` n `26`; metal avg `-0.1365` n `20`; unknown avg `0.1721` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
