# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T06:07:27.149459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0691` n `13`; crypto_alt avg `-0.4304` n `237`; crypto_major avg `-0.1651` n `8`; equity avg `-0.2642` n `152`; fx avg `0.0145` n `6`; index avg `-0.0336` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.0835` n `1212`
- 1h: commodity avg `-0.0208` n `13`; crypto_alt avg `-0.2557` n `237`; crypto_major avg `-0.0037` n `8`; equity avg `-0.2323` n `152`; fx avg `0.0211` n `6`; index avg `-0.0652` n `26`; metal avg `-0.0804` n `20`; unknown avg `0.3958` n `1212`
- 4h: commodity avg `-0.0585` n `13`; crypto_alt avg `-0.0409` n `237`; crypto_major avg `0.0001` n `8`; equity avg `-0.0484` n `152`; fx avg `0.0055` n `6`; index avg `-0.0263` n `26`; metal avg `0.0446` n `20`; unknown avg `0.841` n `1196`
- 24h: commodity avg `-0.6039` n `13`; crypto_alt avg `-0.6598` n `237`; crypto_major avg `-0.4363` n `8`; equity avg `-0.4165` n `152`; fx avg `0.073` n `6`; index avg `-0.0051` n `26`; metal avg `0.163` n `20`; unknown avg `-0.264` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.256`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
