# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T05:52:27.876870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.1951` n `235`; crypto_major avg `-0.212` n `8`; equity avg `-0.0087` n `149`; fx avg `-0.0074` n `6`; index avg `0.0036` n `26`; metal avg `-0.0229` n `20`; unknown avg `0.0766` n `1074`
- 1h: commodity avg `-0.0259` n `13`; crypto_alt avg `0.0617` n `235`; crypto_major avg `-0.1058` n `8`; equity avg `0.1148` n `149`; fx avg `-0.0338` n `6`; index avg `0.0354` n `26`; metal avg `-0.0132` n `20`; unknown avg `-0.2803` n `1070`
- 4h: commodity avg `0.0521` n `13`; crypto_alt avg `-0.3437` n `235`; crypto_major avg `-0.3506` n `8`; equity avg `0.0411` n `149`; fx avg `-0.0223` n `6`; index avg `0.0188` n `26`; metal avg `-0.1094` n `20`; unknown avg `-0.1197` n `1062`
- 24h: commodity avg `0.0406` n `13`; crypto_alt avg `-0.6307` n `235`; crypto_major avg `-0.0914` n `8`; equity avg `0.2332` n `149`; fx avg `0.008` n `6`; index avg `0.1512` n `26`; metal avg `-0.057` n `20`; unknown avg `587.2657` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
