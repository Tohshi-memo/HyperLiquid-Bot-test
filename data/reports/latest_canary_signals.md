# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T12:37:28.596123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1275` n `12`; crypto_alt avg `-0.0719` n `230`; crypto_major avg `-0.1344` n `8`; equity avg `-0.1836` n `96`; fx avg `-0.0069` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0236` n `20`; unknown avg `0.0157` n `769`
- 1h: commodity avg `0.0858` n `12`; crypto_alt avg `-0.1956` n `230`; crypto_major avg `-0.311` n `8`; equity avg `-0.5461` n `96`; fx avg `-0.0295` n `6`; index avg `-0.0646` n `25`; metal avg `-0.0977` n `20`; unknown avg `0.0916` n `769`
- 4h: commodity avg `0.3788` n `12`; crypto_alt avg `0.5182` n `230`; crypto_major avg `0.4088` n `8`; equity avg `0.789` n `96`; fx avg `-0.0347` n `6`; index avg `0.1033` n `25`; metal avg `-0.0434` n `20`; unknown avg `0.2545` n `768`
- 24h: commodity avg `-0.1246` n `12`; crypto_alt avg `-1.5173` n `230`; crypto_major avg `-2.4463` n `8`; equity avg `-4.4277` n `94`; fx avg `-0.0401` n `6`; index avg `-0.5213` n `25`; metal avg `-0.6472` n `20`; unknown avg `-0.3259` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
