# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T20:22:33.411924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.2603` n `237`; crypto_major avg `0.2296` n `8`; equity avg `0.0391` n `151`; fx avg `-0.0042` n `6`; index avg `0.0111` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.792` n `1162`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `0.2817` n `237`; crypto_major avg `0.2547` n `8`; equity avg `-0.1852` n `151`; fx avg `-0.0072` n `6`; index avg `-0.0359` n `26`; metal avg `-0.0462` n `20`; unknown avg `-0.0995` n `1128`
- 4h: commodity avg `-0.1894` n `13`; crypto_alt avg `0.0046` n `237`; crypto_major avg `0.0895` n `8`; equity avg `-0.6344` n `151`; fx avg `0.0005` n `6`; index avg `-0.087` n `26`; metal avg `-0.0328` n `20`; unknown avg `-0.1933` n `1128`
- 24h: commodity avg `-0.3` n `13`; crypto_alt avg `3.2544` n `237`; crypto_major avg `2.517` n `8`; equity avg `2.8538` n `151`; fx avg `0.0116` n `6`; index avg `0.574` n `26`; metal avg `0.11` n `20`; unknown avg `3.1776` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
