# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T00:07:34.428713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.057` n `12`; crypto_alt avg `-0.0046` n `234`; crypto_major avg `-0.0702` n `8`; equity avg `-0.1371` n `140`; fx avg `0.0152` n `6`; index avg `-0.0212` n `26`; metal avg `0.0083` n `20`; unknown avg `0.1027` n `937`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `0.0385` n `234`; crypto_major avg `-0.4` n `8`; equity avg `-0.044` n `140`; fx avg `-0.0386` n `6`; index avg `-0.0108` n `26`; metal avg `0.0069` n `20`; unknown avg `0.5563` n `937`
- 4h: commodity avg `0.0979` n `12`; crypto_alt avg `1.5095` n `234`; crypto_major avg `0.1682` n `8`; equity avg `0.087` n `140`; fx avg `-0.0404` n `6`; index avg `-0.0097` n `26`; metal avg `0.0239` n `20`; unknown avg `0.3514` n `906`
- 24h: commodity avg `0.1716` n `12`; crypto_alt avg `2.9963` n `234`; crypto_major avg `0.529` n `8`; equity avg `0.4647` n `140`; fx avg `-0.2685` n `6`; index avg `0.0569` n `26`; metal avg `0.121` n `20`; unknown avg `1.3246` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
