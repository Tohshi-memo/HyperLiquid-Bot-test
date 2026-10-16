# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T00:22:26.598269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `13`; crypto_alt avg `-0.1745` n `236`; crypto_major avg `-0.0632` n `8`; equity avg `-0.4598` n `151`; fx avg `0.004` n `6`; index avg `-0.0532` n `26`; metal avg `-0.0305` n `20`; unknown avg `0.5878` n `1136`
- 1h: commodity avg `0.0227` n `13`; crypto_alt avg `0.3757` n `236`; crypto_major avg `0.1874` n `8`; equity avg `-0.6964` n `151`; fx avg `0.0099` n `6`; index avg `-0.1164` n `26`; metal avg `-0.0692` n `20`; unknown avg `0.7294` n `1128`
- 4h: commodity avg `-0.0593` n `13`; crypto_alt avg `-0.1835` n `236`; crypto_major avg `-0.4279` n `8`; equity avg `-1.026` n `151`; fx avg `-0.0076` n `6`; index avg `-0.189` n `26`; metal avg `-0.1229` n `20`; unknown avg `0.0016` n `1082`
- 24h: commodity avg `-0.2013` n `13`; crypto_alt avg `0.4903` n `236`; crypto_major avg `0.1847` n `8`; equity avg `0.5504` n `151`; fx avg `0.0384` n `6`; index avg `0.0467` n `26`; metal avg `0.2174` n `20`; unknown avg `25.0669` n `910`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0968`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0799`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0614`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
