# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T17:07:50.864500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1401` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6827` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.158` n `237`; crypto_major avg `0.0535` n `8`; equity avg `-0.0788` n `151`; fx avg `-0.0131` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0255` n `20`; unknown avg `-0.1441` n `1197`
- 1h: commodity avg `0.1455` n `13`; crypto_alt avg `0.3764` n `237`; crypto_major avg `0.3615` n `8`; equity avg `-0.1843` n `151`; fx avg `-0.0132` n `6`; index avg `-0.0439` n `26`; metal avg `-0.0594` n `20`; unknown avg `29.8612` n `1197`
- 4h: commodity avg `-0.3227` n `13`; crypto_alt avg `2.7012` n `237`; crypto_major avg `1.8174` n `8`; equity avg `1.6653` n `151`; fx avg `0.0245` n `6`; index avg `0.2206` n `26`; metal avg `0.1347` n `20`; unknown avg `4.109` n `1100`
- 24h: commodity avg `-0.4029` n `13`; crypto_alt avg `2.8503` n `237`; crypto_major avg `1.7106` n `8`; equity avg `-0.0332` n `151`; fx avg `0.0247` n `6`; index avg `-0.0161` n `26`; metal avg `0.0037` n `20`; unknown avg `3.611` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
