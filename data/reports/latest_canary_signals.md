# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T09:07:28.954329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.36` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.0838` n `234`; crypto_major avg `0.0073` n `8`; equity avg `-0.0009` n `140`; fx avg `0.0249` n `6`; index avg `0.0014` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.1219` n `940`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.6499` n `234`; crypto_major avg `0.2432` n `8`; equity avg `0.0253` n `140`; fx avg `0.0115` n `6`; index avg `0.0241` n `26`; metal avg `-0.0079` n `20`; unknown avg `1.9828` n `940`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `0.4076` n `234`; crypto_major avg `0.0523` n `8`; equity avg `-0.0246` n `140`; fx avg `0.0237` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0193` n `20`; unknown avg `1.9501` n `898`
- 24h: commodity avg `0.3151` n `12`; crypto_alt avg `3.3188` n `234`; crypto_major avg `3.6716` n `8`; equity avg `0.1264` n `140`; fx avg `-0.0194` n `6`; index avg `-0.0466` n `26`; metal avg `-0.2821` n `20`; unknown avg `2.3592` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
