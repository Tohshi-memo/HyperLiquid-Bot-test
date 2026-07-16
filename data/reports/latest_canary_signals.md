# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T04:29:02.404755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.0281` n `230`; crypto_major avg `0.065` n `8`; equity avg `-0.1154` n `94`; fx avg `0.0101` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.1942` n `768`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.097` n `230`; crypto_major avg `-0.0927` n `8`; equity avg `-0.1977` n `94`; fx avg `0.0046` n `6`; index avg `-0.0099` n `25`; metal avg `0.0557` n `20`; unknown avg `0.0229` n `768`
- 4h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.0989` n `230`; crypto_major avg `-0.1594` n `8`; equity avg `-0.1266` n `94`; fx avg `-0.014` n `6`; index avg `-0.071` n `25`; metal avg `-0.1617` n `20`; unknown avg `-0.5471` n `768`
- 24h: commodity avg `-0.0641` n `12`; crypto_alt avg `0.1524` n `230`; crypto_major avg `0.0916` n `8`; equity avg `-2.5307` n `93`; fx avg `0.1136` n `6`; index avg `-0.4827` n `25`; metal avg `0.0325` n `20`; unknown avg `-0.1547` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
