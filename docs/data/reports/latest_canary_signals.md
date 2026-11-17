# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T04:07:38.905358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `13`; crypto_alt avg `-0.0007` n `239`; crypto_major avg `-0.0808` n `8`; equity avg `-0.2916` n `162`; fx avg `-0.0019` n `6`; index avg `-0.0481` n `27`; metal avg `-0.0249` n `20`; unknown avg `201.4584` n `1252`
- 1h: commodity avg `-0.1045` n `13`; crypto_alt avg `0.4851` n `239`; crypto_major avg `0.6074` n `8`; equity avg `-0.2628` n `162`; fx avg `-0.0143` n `6`; index avg `-0.0796` n `27`; metal avg `-0.0921` n `20`; unknown avg `0.1428` n `1252`
- 4h: commodity avg `-0.2105` n `13`; crypto_alt avg `0.7436` n `239`; crypto_major avg `0.7988` n `8`; equity avg `0.5259` n `162`; fx avg `0.0241` n `6`; index avg `0.019` n `27`; metal avg `0.1662` n `20`; unknown avg `0.0863` n `1252`
- 24h: commodity avg `-1.211` n `13`; crypto_alt avg `0.7093` n `239`; crypto_major avg `1.2315` n `8`; equity avg `-2.4887` n `162`; fx avg `-0.0337` n `6`; index avg `-0.2716` n `27`; metal avg `-0.0946` n `20`; unknown avg `557.6288` n `993`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
