# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T03:37:27.928604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `13`; crypto_alt avg `0.6246` n `238`; crypto_major avg `0.7515` n `8`; equity avg `0.2237` n `156`; fx avg `-0.0036` n `6`; index avg `0.0143` n `27`; metal avg `0.0218` n `20`; unknown avg `5.781` n `1256`
- 1h: commodity avg `-0.0316` n `13`; crypto_alt avg `0.3585` n `238`; crypto_major avg `0.5959` n `8`; equity avg `0.2108` n `156`; fx avg `-0.0564` n `6`; index avg `0.0085` n `27`; metal avg `-0.0592` n `20`; unknown avg `0.744` n `1250`
- 4h: commodity avg `0.1376` n `13`; crypto_alt avg `-0.9347` n `238`; crypto_major avg `0.0869` n `8`; equity avg `-0.1914` n `156`; fx avg `-0.0489` n `6`; index avg `-0.1318` n `27`; metal avg `-0.267` n `20`; unknown avg `1.0056` n `1234`
- 24h: commodity avg `-0.0502` n `13`; crypto_alt avg `-4.2886` n `238`; crypto_major avg `-0.1954` n `8`; equity avg `-2.6094` n `155`; fx avg `0.135` n `6`; index avg `-0.2796` n `27`; metal avg `-0.6322` n `20`; unknown avg `28.7457` n `982`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
