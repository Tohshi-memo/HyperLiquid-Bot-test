# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T09:37:18.971016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2633` n `12`; crypto_alt avg `-0.3163` n `228`; crypto_major avg `-0.2567` n `8`; equity avg `-0.0852` n `67`; fx avg `0.0003` n `6`; index avg `-0.0672` n `23`; metal avg `0.3874` n `18`; unknown avg `0.1088` n `386`
- 1h: commodity avg `-0.3283` n `12`; crypto_alt avg `-0.04` n `228`; crypto_major avg `0.0603` n `8`; equity avg `-0.4796` n `67`; fx avg `-0.0137` n `6`; index avg `-0.1743` n `23`; metal avg `0.1323` n `18`; unknown avg `-0.4517` n `386`
- 4h: commodity avg `0.1635` n `12`; crypto_alt avg `-0.0808` n `228`; crypto_major avg `0.0776` n `8`; equity avg `-0.5652` n `67`; fx avg `-0.0184` n `6`; index avg `-0.1535` n `23`; metal avg `-0.4413` n `18`; unknown avg `-0.4239` n `376`
- 24h: commodity avg `0.148` n `12`; crypto_alt avg `1.6356` n `228`; crypto_major avg `0.0241` n `8`; equity avg `0.6733` n `67`; fx avg `0.1013` n `6`; index avg `0.4361` n `23`; metal avg `0.288` n `18`; unknown avg `0.8343` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0354`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0344`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0333`, n `668`, weak_sample_signal
