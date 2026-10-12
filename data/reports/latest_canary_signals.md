# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T09:37:36.076698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `13`; crypto_alt avg `-0.1691` n `235`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0233` n `151`; fx avg `0.003` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0099` n `20`; unknown avg `0.0552` n `1115`
- 1h: commodity avg `0.1533` n `13`; crypto_alt avg `-0.3374` n `235`; crypto_major avg `-0.3346` n `8`; equity avg `-0.1565` n `151`; fx avg `0.002` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.1686` n `1049`
- 4h: commodity avg `0.3371` n `13`; crypto_alt avg `-0.7351` n `235`; crypto_major avg `-0.4132` n `8`; equity avg `-0.7051` n `151`; fx avg `-0.065` n `6`; index avg `-0.0945` n `26`; metal avg `-0.0578` n `20`; unknown avg `0.7211` n `989`
- 24h: commodity avg `-0.0808` n `13`; crypto_alt avg `1.8414` n `235`; crypto_major avg `1.2692` n `8`; equity avg `-1.078` n `151`; fx avg `-0.1086` n `6`; index avg `-0.1201` n `26`; metal avg `0.0004` n `20`; unknown avg `0.1077` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
