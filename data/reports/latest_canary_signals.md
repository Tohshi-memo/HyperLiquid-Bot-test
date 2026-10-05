# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T21:52:32.141802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `0.047` n `235`; crypto_major avg `0.0417` n `8`; equity avg `0.005` n `144`; fx avg `-0.0013` n `6`; index avg `-0.0129` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.0445` n `1055`
- 1h: commodity avg `-0.0219` n `13`; crypto_alt avg `0.4386` n `235`; crypto_major avg `0.2046` n `8`; equity avg `0.0427` n `144`; fx avg `-0.0103` n `6`; index avg `0.0111` n `26`; metal avg `0.0119` n `20`; unknown avg `2.1675` n `1025`
- 4h: commodity avg `-0.0644` n `13`; crypto_alt avg `1.1773` n `235`; crypto_major avg `0.6206` n `8`; equity avg `0.0599` n `144`; fx avg `-0.0002` n `6`; index avg `0.0238` n `26`; metal avg `0.0309` n `20`; unknown avg `2.874` n `979`
- 24h: commodity avg `-0.3458` n `13`; crypto_alt avg `0.8749` n `235`; crypto_major avg `0.208` n `8`; equity avg `0.3415` n `144`; fx avg `-0.1076` n `6`; index avg `0.1336` n `26`; metal avg `0.1909` n `20`; unknown avg `630.4893` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1996`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1799`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.171`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1265`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `669`, weak_sample_signal
