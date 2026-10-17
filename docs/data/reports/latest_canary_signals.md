# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T18:52:26.656738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.1231` n `236`; crypto_major avg `0.0266` n `8`; equity avg `0.0382` n `151`; fx avg `0.0032` n `6`; index avg `0.008` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.0327` n `1193`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `0.768` n `236`; crypto_major avg `0.3331` n `8`; equity avg `0.2125` n `151`; fx avg `-0.0046` n `6`; index avg `0.0369` n `26`; metal avg `0.0149` n `20`; unknown avg `1.3796` n `1183`
- 4h: commodity avg `0.0666` n `13`; crypto_alt avg `-0.3237` n `236`; crypto_major avg `-0.3015` n `8`; equity avg `-0.1036` n `151`; fx avg `-0.0241` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0241` n `20`; unknown avg `1.8812` n `1137`
- 24h: commodity avg `0.0341` n `13`; crypto_alt avg `-0.4829` n `236`; crypto_major avg `0.3059` n `8`; equity avg `-0.131` n `151`; fx avg `-0.0178` n `6`; index avg `-0.0212` n `26`; metal avg `0.0369` n `20`; unknown avg `2.2996` n `1019`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1718`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1475`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0729`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
