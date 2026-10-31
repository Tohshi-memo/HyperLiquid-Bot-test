# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T10:37:27.907257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `13`; crypto_alt avg `0.0372` n `238`; crypto_major avg `0.1037` n `8`; equity avg `-0.015` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0001` n `20`; unknown avg `5.0564` n `1262`
- 1h: commodity avg `0.0205` n `13`; crypto_alt avg `0.0003` n `238`; crypto_major avg `0.1903` n `8`; equity avg `-0.0296` n `156`; fx avg `0.0091` n `6`; index avg `-0.0059` n `27`; metal avg `0.0082` n `20`; unknown avg `-0.1449` n `1256`
- 4h: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.2269` n `238`; crypto_major avg `0.0126` n `8`; equity avg `-0.0406` n `156`; fx avg `0.0193` n `6`; index avg `-0.012` n `27`; metal avg `-0.0099` n `20`; unknown avg `5.0594` n `1236`
- 24h: commodity avg `-0.2603` n `13`; crypto_alt avg `0.2627` n `238`; crypto_major avg `-0.9693` n `8`; equity avg `-1.7284` n `156`; fx avg `-0.0941` n `6`; index avg `-0.1626` n `27`; metal avg `-0.3873` n `20`; unknown avg `4.5759` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
