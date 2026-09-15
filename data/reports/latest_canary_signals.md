# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T17:37:27.918906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `1.1255` n `233`; crypto_major avg `1.1348` n `8`; equity avg `0.1229` n `137`; fx avg `0.0111` n `6`; index avg `0.0144` n `27`; metal avg `0.0449` n `20`; unknown avg `0.6634` n `917`
- 1h: commodity avg `0.0878` n `12`; crypto_alt avg `0.9054` n `233`; crypto_major avg `0.9561` n `8`; equity avg `0.0304` n `137`; fx avg `0.0185` n `6`; index avg `-0.0004` n `27`; metal avg `0.0433` n `20`; unknown avg `0.1102` n `915`
- 4h: commodity avg `0.2434` n `12`; crypto_alt avg `0.3455` n `233`; crypto_major avg `-0.0251` n `8`; equity avg `-0.7578` n `137`; fx avg `0.0269` n `6`; index avg `-0.1092` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.607` n `873`
- 24h: commodity avg `0.5781` n `12`; crypto_alt avg `-1.6886` n `233`; crypto_major avg `-1.7936` n `8`; equity avg `-1.3557` n `137`; fx avg `0.2217` n `6`; index avg `-0.1783` n `27`; metal avg `0.0236` n `20`; unknown avg `0.7273` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
