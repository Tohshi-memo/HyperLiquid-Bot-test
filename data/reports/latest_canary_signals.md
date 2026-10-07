# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T08:52:27.402491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `13`; crypto_alt avg `-0.2744` n `235`; crypto_major avg `-0.1658` n `8`; equity avg `-0.0892` n `150`; fx avg `0.0046` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0836` n `20`; unknown avg `-0.1326` n `1076`
- 1h: commodity avg `-0.1221` n `13`; crypto_alt avg `-0.5705` n `235`; crypto_major avg `-0.278` n `8`; equity avg `-0.1726` n `150`; fx avg `-0.0174` n `6`; index avg `0.007` n `26`; metal avg `-0.0995` n `20`; unknown avg `-0.2677` n `1058`
- 4h: commodity avg `0.0275` n `13`; crypto_alt avg `0.2041` n `235`; crypto_major avg `0.2836` n `8`; equity avg `-0.3769` n `150`; fx avg `-0.0929` n `6`; index avg `-0.0603` n `26`; metal avg `-0.2245` n `20`; unknown avg `0.1044` n `1036`
- 24h: commodity avg `0.9027` n `13`; crypto_alt avg `-3.6824` n `235`; crypto_major avg `-2.3949` n `8`; equity avg `-0.56` n `149`; fx avg `-0.0707` n `6`; index avg `-0.1493` n `26`; metal avg `-0.3535` n `20`; unknown avg `814.6232` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
