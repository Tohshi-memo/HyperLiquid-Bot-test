# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T12:22:43.014795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1066` n `13`; crypto_alt avg `-0.1123` n `239`; crypto_major avg `-0.0983` n `8`; equity avg `-0.2011` n `164`; fx avg `-0.0122` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0313` n `20`; unknown avg `0.3364` n `1264`
- 1h: commodity avg `0.1339` n `13`; crypto_alt avg `-0.0495` n `239`; crypto_major avg `-0.0011` n `8`; equity avg `-0.0578` n `164`; fx avg `-0.0395` n `6`; index avg `0.0074` n `27`; metal avg `-0.0933` n `20`; unknown avg `0.7345` n `1258`
- 4h: commodity avg `0.1692` n `13`; crypto_alt avg `0.1166` n `239`; crypto_major avg `0.0943` n `8`; equity avg `0.3479` n `164`; fx avg `-0.0024` n `6`; index avg `0.0945` n `27`; metal avg `-0.132` n `20`; unknown avg `199.7298` n `1254`
- 24h: commodity avg `0.0919` n `13`; crypto_alt avg `0.1167` n `239`; crypto_major avg `-0.2472` n `8`; equity avg `0.6586` n `164`; fx avg `0.0222` n `6`; index avg `0.2727` n `27`; metal avg `-0.3555` n `20`; unknown avg `2.6043` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
