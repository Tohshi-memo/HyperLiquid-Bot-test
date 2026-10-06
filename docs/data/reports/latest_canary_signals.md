# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T14:37:38.348221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `0.1918` n `235`; crypto_major avg `0.0048` n `8`; equity avg `-0.285` n `150`; fx avg `0.0125` n `6`; index avg `-0.037` n `26`; metal avg `0.043` n `20`; unknown avg `0.5194` n `1050`
- 1h: commodity avg `0.0867` n `13`; crypto_alt avg `0.0064` n `235`; crypto_major avg `-0.0885` n `8`; equity avg `-0.122` n `150`; fx avg `0.0061` n `6`; index avg `-0.0156` n `26`; metal avg `-0.1072` n `20`; unknown avg `0.3713` n `1024`
- 4h: commodity avg `0.2024` n `13`; crypto_alt avg `0.0481` n `235`; crypto_major avg `0.1929` n `8`; equity avg `0.1694` n `150`; fx avg `0.0332` n `6`; index avg `0.0159` n `26`; metal avg `-0.1305` n `20`; unknown avg `1.5396` n `1018`
- 24h: commodity avg `-0.4472` n `13`; crypto_alt avg `0.4883` n `235`; crypto_major avg `0.3659` n `8`; equity avg `0.8268` n `149`; fx avg `0.1344` n `6`; index avg `0.134` n `26`; metal avg `-0.0937` n `20`; unknown avg `390.6953` n `882`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
