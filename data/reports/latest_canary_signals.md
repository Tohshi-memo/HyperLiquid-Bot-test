# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T03:22:25.808088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `-0.0852` n `8`; equity avg `0.0037` n `114`; fx avg `0.0108` n `6`; index avg `-0.0` n `25`; metal avg `-0.0317` n `20`; unknown avg `-0.029` n `792`
- 1h: commodity avg `-0.0922` n `12`; crypto_alt avg `0.3282` n `230`; crypto_major avg `0.3276` n `8`; equity avg `0.2678` n `114`; fx avg `0.0208` n `6`; index avg `0.0234` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.2112` n `792`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `0.7342` n `230`; crypto_major avg `1.0195` n `8`; equity avg `0.5346` n `114`; fx avg `-0.0213` n `6`; index avg `0.0317` n `25`; metal avg `0.1588` n `20`; unknown avg `0.5271` n `791`
- 24h: commodity avg `-0.1672` n `12`; crypto_alt avg `0.2098` n `230`; crypto_major avg `0.518` n `8`; equity avg `0.7142` n `114`; fx avg `-0.0279` n `6`; index avg `0.0741` n `25`; metal avg `0.2004` n `20`; unknown avg `-0.0094` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
