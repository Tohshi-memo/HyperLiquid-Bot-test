# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T21:52:27.156516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7413` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6517` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.5726` n `12`; crypto_alt avg `-0.6129` n `228`; crypto_major avg `-0.5019` n `8`; equity avg `0.0254` n `69`; fx avg `0.0053` n `6`; index avg `0.0079` n `23`; metal avg `-0.002` n `18`; unknown avg `0.3349` n `422`
- 1h: commodity avg `-0.0663` n `12`; crypto_alt avg `-0.0625` n `228`; crypto_major avg `-0.2899` n `8`; equity avg `0.0939` n `69`; fx avg `-0.019` n `6`; index avg `0.0546` n `23`; metal avg `0.0012` n `18`; unknown avg `1.1481` n `422`
- 4h: commodity avg `-0.1503` n `12`; crypto_alt avg `-0.7724` n `228`; crypto_major avg `-1.317` n `8`; equity avg `0.4243` n `69`; fx avg `-0.0124` n `6`; index avg `0.3347` n `23`; metal avg `0.11` n `18`; unknown avg `-0.0662` n `422`
- 24h: commodity avg `-0.3169` n `12`; crypto_alt avg `-3.2128` n `228`; crypto_major avg `-4.6748` n `8`; equity avg `1.0689` n `69`; fx avg `0.0733` n `6`; index avg `0.8122` n `23`; metal avg `0.4076` n `18`; unknown avg `0.5523` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
