# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T23:22:32.263138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0936` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.1644` n `228`; crypto_major avg `-0.2309` n `8`; equity avg `-0.001` n `74`; fx avg `-0.0046` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0044` n `18`; unknown avg `0.004` n `643`
- 1h: commodity avg `-0.2221` n `12`; crypto_alt avg `-0.5081` n `228`; crypto_major avg `-0.5276` n `8`; equity avg `0.0528` n `74`; fx avg `0.0107` n `6`; index avg `-0.076` n `23`; metal avg `0.0239` n `18`; unknown avg `-0.0431` n `643`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `-0.6982` n `228`; crypto_major avg `-1.007` n `8`; equity avg `-0.0055` n `74`; fx avg `-0.0063` n `6`; index avg `0.0866` n `23`; metal avg `0.0836` n `18`; unknown avg `0.5442` n `643`
- 24h: commodity avg `-0.6638` n `12`; crypto_alt avg `-0.5699` n `228`; crypto_major avg `-0.273` n `8`; equity avg `-0.4669` n `74`; fx avg `-0.0107` n `6`; index avg `0.2968` n `23`; metal avg `0.2555` n `18`; unknown avg `41.4551` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
