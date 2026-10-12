# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T05:52:31.022070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6399` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0377` n `13`; crypto_alt avg `0.1776` n `235`; crypto_major avg `0.2057` n `8`; equity avg `-0.015` n `151`; fx avg `-0.0002` n `6`; index avg `0.0038` n `26`; metal avg `0.0249` n `20`; unknown avg `3.918` n `1125`
- 1h: commodity avg `0.0787` n `13`; crypto_alt avg `-0.0085` n `235`; crypto_major avg `-0.0528` n `8`; equity avg `-0.2101` n `151`; fx avg `0.0026` n `6`; index avg `-0.039` n `26`; metal avg `-0.0309` n `20`; unknown avg `1.7581` n `1123`
- 4h: commodity avg `0.1125` n `13`; crypto_alt avg `1.3654` n `235`; crypto_major avg `0.9766` n `8`; equity avg `-0.6633` n `151`; fx avg `-0.0034` n `6`; index avg `-0.0556` n `26`; metal avg `-0.0905` n `20`; unknown avg `-0.0939` n `1043`
- 24h: commodity avg `-0.3208` n `13`; crypto_alt avg `3.1077` n `235`; crypto_major avg `1.8938` n `8`; equity avg `-0.3234` n `151`; fx avg `-0.0421` n `6`; index avg `-0.0142` n `26`; metal avg `0.0947` n `20`; unknown avg `0.7156` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
