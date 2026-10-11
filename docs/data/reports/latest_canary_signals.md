# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T21:07:33.407871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.2803` n `235`; crypto_major avg `-0.1381` n `8`; equity avg `-0.0323` n `150`; fx avg `-0.0275` n `6`; index avg `-0.0035` n `26`; metal avg `0.0015` n `20`; unknown avg `0.2981` n `1126`
- 1h: commodity avg `0.0536` n `13`; crypto_alt avg `-0.3146` n `235`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0117` n `150`; fx avg `-0.0281` n `6`; index avg `-0.0037` n `26`; metal avg `0.0062` n `20`; unknown avg `0.0315` n `1126`
- 4h: commodity avg `0.1246` n `13`; crypto_alt avg `-0.3203` n `235`; crypto_major avg `-0.3744` n `8`; equity avg `-0.0334` n `150`; fx avg `-0.0266` n `6`; index avg `-0.0029` n `26`; metal avg `0.0007` n `20`; unknown avg `0.2443` n `1094`
- 24h: commodity avg `0.3689` n `13`; crypto_alt avg `1.3299` n `235`; crypto_major avg `0.4932` n `8`; equity avg `0.2402` n `150`; fx avg `-0.0009` n `6`; index avg `0.0255` n `26`; metal avg `0.0847` n `20`; unknown avg `0.7139` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
