# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T03:07:31.715444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `13`; crypto_alt avg `0.0393` n `234`; crypto_major avg `0.1054` n `8`; equity avg `0.0687` n `142`; fx avg `0.0053` n `6`; index avg `0.0047` n `26`; metal avg `0.0556` n `20`; unknown avg `-0.0855` n `983`
- 1h: commodity avg `-0.0349` n `13`; crypto_alt avg `0.2337` n `234`; crypto_major avg `0.2383` n `8`; equity avg `0.1421` n `142`; fx avg `-0.0013` n `6`; index avg `0.0174` n `26`; metal avg `0.1436` n `20`; unknown avg `1.4352` n `983`
- 4h: commodity avg `-0.174` n `13`; crypto_alt avg `1.0372` n `234`; crypto_major avg `0.8252` n `8`; equity avg `0.1359` n `142`; fx avg `-0.0101` n `6`; index avg `0.0358` n `26`; metal avg `-0.0237` n `20`; unknown avg `0.6199` n `977`
- 24h: commodity avg `0.0419` n `13`; crypto_alt avg `-0.0992` n `234`; crypto_major avg `0.6836` n `8`; equity avg `0.7091` n `142`; fx avg `-0.2126` n `6`; index avg `0.0667` n `26`; metal avg `-0.0982` n `20`; unknown avg `0.3388` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
