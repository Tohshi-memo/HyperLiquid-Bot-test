# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T15:37:28.786732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0627` n `13`; crypto_alt avg `-0.0081` n `239`; crypto_major avg `-0.0732` n `8`; equity avg `0.2892` n `156`; fx avg `-0.0189` n `6`; index avg `-0.0033` n `27`; metal avg `-0.0399` n `20`; unknown avg `0.4194` n `1263`
- 1h: commodity avg `-0.0581` n `13`; crypto_alt avg `-0.0565` n `239`; crypto_major avg `-0.0718` n `8`; equity avg `1.1804` n `156`; fx avg `-0.0004` n `6`; index avg `0.133` n `27`; metal avg `0.0237` n `20`; unknown avg `16.0477` n `1257`
- 4h: commodity avg `-0.3856` n `13`; crypto_alt avg `0.1554` n `238`; crypto_major avg `0.0676` n `8`; equity avg `-0.5205` n `156`; fx avg `0.0051` n `6`; index avg `0.0683` n `27`; metal avg `0.2959` n `20`; unknown avg `44.0443` n `1252`
- 24h: commodity avg `-0.9538` n `13`; crypto_alt avg `-1.9677` n `238`; crypto_major avg `-0.5509` n `8`; equity avg `0.2887` n `156`; fx avg `0.2709` n `6`; index avg `0.312` n `27`; metal avg `0.3403` n `20`; unknown avg `8.0051` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
