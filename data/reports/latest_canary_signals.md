# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T15:07:38.405750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.1234` n `238`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0253` n `156`; fx avg `-0.0031` n `6`; index avg `-0.0031` n `27`; metal avg `0.0` n `20`; unknown avg `0.4237` n `1256`
- 1h: commodity avg `-0.0403` n `13`; crypto_alt avg `0.2976` n `238`; crypto_major avg `0.0069` n `8`; equity avg `0.0852` n `156`; fx avg `0.0049` n `6`; index avg `0.0104` n `27`; metal avg `0.0106` n `20`; unknown avg `0.1451` n `1256`
- 4h: commodity avg `-0.1237` n `13`; crypto_alt avg `0.629` n `238`; crypto_major avg `-0.0057` n `8`; equity avg `0.061` n `156`; fx avg `-0.004` n `6`; index avg `-0.0001` n `27`; metal avg `0.0135` n `20`; unknown avg `234.9077` n `1238`
- 24h: commodity avg `-0.3039` n `13`; crypto_alt avg `0.3979` n `238`; crypto_major avg `-0.8655` n `8`; equity avg `-0.4885` n `156`; fx avg `0.0449` n `6`; index avg `-0.11` n `27`; metal avg `-0.0945` n `20`; unknown avg `0.6108` n `1099`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
