# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T00:52:31.921623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0259` n `13`; crypto_alt avg `0.1261` n `235`; crypto_major avg `0.1622` n `8`; equity avg `-0.0175` n `150`; fx avg `-0.0159` n `6`; index avg `-0.0162` n `26`; metal avg `0.0684` n `20`; unknown avg `0.1658` n `1077`
- 1h: commodity avg `0.0574` n `13`; crypto_alt avg `0.2515` n `235`; crypto_major avg `0.1637` n `8`; equity avg `-0.1464` n `150`; fx avg `-0.069` n `6`; index avg `-0.0836` n `26`; metal avg `0.0359` n `20`; unknown avg `0.0732` n `1069`
- 4h: commodity avg `0.1254` n `13`; crypto_alt avg `0.953` n `235`; crypto_major avg `0.2786` n `8`; equity avg `0.0196` n `150`; fx avg `-0.0499` n `6`; index avg `-0.0335` n `26`; metal avg `0.0673` n `20`; unknown avg `0.0212` n `1061`
- 24h: commodity avg `0.3902` n `13`; crypto_alt avg `-3.2588` n `235`; crypto_major avg `-3.0838` n `8`; equity avg `-1.5089` n `150`; fx avg `-0.2255` n `6`; index avg `-0.2852` n `26`; metal avg `-0.6127` n `20`; unknown avg `247.8405` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
