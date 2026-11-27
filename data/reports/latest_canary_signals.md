# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T02:37:26.268101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `0.4592` n `239`; crypto_major avg `0.6582` n `8`; equity avg `0.5325` n `168`; fx avg `0.003` n `6`; index avg `0.042` n `27`; metal avg `0.2152` n `20`; unknown avg `-0.0938` n `1261`
- 1h: commodity avg `0.0552` n `13`; crypto_alt avg `1.2198` n `239`; crypto_major avg `1.6682` n `8`; equity avg `1.1078` n `168`; fx avg `0.001` n `6`; index avg `0.0922` n `27`; metal avg `0.7623` n `20`; unknown avg `0.0264` n `1259`
- 4h: commodity avg `0.1911` n `13`; crypto_alt avg `1.5472` n `239`; crypto_major avg `1.9537` n `8`; equity avg `2.0837` n `168`; fx avg `-0.0172` n `6`; index avg `0.2109` n `27`; metal avg `0.8977` n `20`; unknown avg `0.0949` n `1211`
- 24h: commodity avg `0.2357` n `13`; crypto_alt avg `1.582` n `239`; crypto_major avg `1.7349` n `8`; equity avg `1.6736` n `168`; fx avg `0.0261` n `6`; index avg `0.1579` n `27`; metal avg `0.5439` n `20`; unknown avg `181.9072` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
