# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T09:37:28.088030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `-0.1969` n `235`; crypto_major avg `-0.1791` n `8`; equity avg `0.0149` n `150`; fx avg `-0.0202` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0332` n `20`; unknown avg `0.0028` n `1076`
- 1h: commodity avg `0.0588` n `13`; crypto_alt avg `-0.8212` n `235`; crypto_major avg `-0.6682` n `8`; equity avg `-0.3918` n `150`; fx avg `-0.0125` n `6`; index avg `-0.0468` n `26`; metal avg `-0.2066` n `20`; unknown avg `0.2591` n `1074`
- 4h: commodity avg `0.0596` n `13`; crypto_alt avg `-0.8127` n `235`; crypto_major avg `-0.5417` n `8`; equity avg `-0.6717` n `150`; fx avg `-0.1028` n `6`; index avg `-0.102` n `26`; metal avg `-0.3035` n `20`; unknown avg `0.2447` n `1036`
- 24h: commodity avg `1.0764` n `13`; crypto_alt avg `-4.0578` n `235`; crypto_major avg `-2.6967` n `8`; equity avg `-0.9531` n `150`; fx avg `-0.099` n `6`; index avg `-0.1906` n `26`; metal avg `-0.5066` n `20`; unknown avg `815.1801` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
