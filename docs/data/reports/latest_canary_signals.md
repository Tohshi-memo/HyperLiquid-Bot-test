# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T19:46:32.690512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9579` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.374` n `234`; crypto_major avg `0.5228` n `8`; equity avg `0.3193` n `137`; fx avg `-0.0028` n `6`; index avg `0.0345` n `27`; metal avg `0.0263` n `20`; unknown avg `3.46` n `917`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.075` n `234`; crypto_major avg `0.4283` n `8`; equity avg `-0.3148` n `137`; fx avg `0.0545` n `6`; index avg `-0.129` n `27`; metal avg `-0.1435` n `20`; unknown avg `18.2223` n `879`
- 4h: commodity avg `-0.0481` n `12`; crypto_alt avg `0.8107` n `234`; crypto_major avg `0.8596` n `8`; equity avg `-1.0983` n `137`; fx avg `0.0415` n `6`; index avg `-0.3142` n `27`; metal avg `-0.6333` n `20`; unknown avg `5.1228` n `869`
- 24h: commodity avg `-0.6743` n `12`; crypto_alt avg `-0.9172` n `234`; crypto_major avg `0.396` n `8`; equity avg `0.5022` n `137`; fx avg `0.0645` n `6`; index avg `-0.024` n `27`; metal avg `-0.32` n `20`; unknown avg `3.1889` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
