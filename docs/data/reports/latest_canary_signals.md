# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T00:52:27.446099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.1758` n `234`; crypto_major avg `-0.1037` n `8`; equity avg `-0.0125` n `141`; fx avg `0.0001` n `6`; index avg `-0.0031` n `26`; metal avg `0.0026` n `20`; unknown avg `7.1114` n `959`
- 1h: commodity avg `-0.0717` n `12`; crypto_alt avg `-0.4862` n `234`; crypto_major avg `-0.2332` n `8`; equity avg `0.0175` n `141`; fx avg `0.0056` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0063` n `20`; unknown avg `13.9899` n `951`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.8641` n `234`; crypto_major avg `0.5992` n `8`; equity avg `0.1541` n `141`; fx avg `-0.0033` n `6`; index avg `0.0059` n `26`; metal avg `0.0061` n `20`; unknown avg `0.4658` n `927`
- 24h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.5787` n `234`; crypto_major avg `-0.5754` n `8`; equity avg `0.2505` n `141`; fx avg `0.0165` n `6`; index avg `0.0137` n `26`; metal avg `0.0111` n `20`; unknown avg `4.7717` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
